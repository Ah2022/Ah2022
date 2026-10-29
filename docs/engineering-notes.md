# From model data to review decisions

[← Back to Ahmed's profile](../README.md)

This page follows the current [BIM Engine source](https://github.com/Ah2022/BIM-Engine). It explains selected implementation decisions rather than claiming measured project savings or complete model coverage.

## 1. Reduce the search space

An octree stores target bounds. Each source queries nearby entries before more expensive solid checks. Candidate search padding guards box boundaries; it is not a clearance rule.

Excerpt from [`CandidatePairFinder.FindCandidates`](https://github.com/Ah2022/BIM-Engine/blob/main/BIMEngine.Core/Spatial/CandidatePairFinder.cs):

```csharp
AABB queryRegion = source.Bounds.Expand(queryPaddingFeet);
List<SpatialEntry> nearby = targetIndex.Query(queryRegion);

```

The linked method then resolves nearby entries, skips self-pairs and collects candidates. A nearby bounding box is a candidate, not evidence of a hard clash.

## 2. Check the actual geometry

The C# core collects host and loaded-link geometry, caches extracted solids and uses Revit Boolean intersections. Unsupported geometry and failed operations require diagnostics. Revit API work runs on Revit's API thread.

[Geometry implementation](https://github.com/Ah2022/BIM-Engine/tree/main/BIMEngine.Core/Geometry) · [Documented scope and limits](https://github.com/Ah2022/BIM-Engine#scope-and-limitations)

## 3. Preserve the review history

The Python bridge stores project identity, scan scope, element identity and issues in SQLite. Reviewed and ignored decisions survive repeat scans. Resolution depends on a complete scan of the same scope; an empty filtered view is not proof that the whole model is clear.

[Database implementation](https://github.com/Ah2022/BIM-Engine/blob/main/BIMEngine.extension/lib/bimengine_core/database.py) · [Dashboard implementation](https://github.com/Ah2022/BIM-Engine/tree/main/BIMEngine.Core/Dashboard)

## 4. Keep engineering calculations traceable

In the separate Plumbing AI Engineer application, calculation functions return inputs, formulas, intermediate values, units and status. For example, the [hydraulics module](https://github.com/Ah2022/Plumbing-AI-Engineer/blob/main/calculations/hydraulics.py) converts flow and internal diameter before calculating velocity. It records a calculated-but-not-approved status, preserving the distinction between a numeric result and engineering acceptance.

The [BIM mapping module](https://github.com/Ah2022/Plumbing-AI-Engineer/blob/main/bim/mapping.py) retains source identities and connector evidence. It does not infer physical connectivity from proximity alone.

## Explore safely with fictional data

The [profile examples](../examples/README.md) are standalone illustrations. They do not contain client models, real issue records or exported production evidence.
