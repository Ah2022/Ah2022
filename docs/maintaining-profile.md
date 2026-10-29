# Maintaining this profile

## Content and evidence

- Edit `README.md` for the profile introduction, skills and project summaries.
- Keep project capability and maturity statements aligned with each linked repository.
- The contact email follows the live portfolio contact section and the previous profile README. The portfolio repository's README lists a different email; reconcile that repository separately if needed.
- The covers and geometry animation are original schematics. Replace them with actual application captures only when recordings are available, then update their captions.
- Do not substitute synthetic examples for actual tool output or project evidence.

## Regenerate the artwork

Use Python 3 with Pillow installed:

```powershell
python scripts/build_assets.py
```

The generator uses Windows Segoe UI fonts, writes to `assets/` and `examples/`, and needs no project model or external image service. The banner has separate light and dark variants. Textual headings, skill descriptions and links remain in Markdown for accessibility and narrow screens.

The contribution snake and externally hosted statistics are no longer embedded in the README. The pre-existing snake workflow is retained; it can be disabled independently if the contribution animation is no longer needed anywhere.

## Before publishing changes

Check the rendered README on GitHub at desktop and narrow widths, expand each details section, inspect both banner variants, open the STL viewer and search the CSV. Verify external destinations and keep each image's alternative text meaningful. The GIF lives behind a collapsed section and has a static alternative.

GitHub provides [expandable sections](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections), [Mermaid diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams), and [STL/CSV viewers](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files). Application interactivity belongs on the linked portfolio; scripts and custom styles are not required by this profile.
