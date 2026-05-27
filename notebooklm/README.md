# NotebookLM Exports

This folder defines small, curated NotebookLM notebooks over the vault.

The goal is not to upload the whole vault. Each notebook should contain a focused guide plus a handful of foundational sources, usually 3-8. Prefer more small notebooks over one mega notebook.

## Files

- `topics.yml` is the curated notebook plan.
- `../scripts/export_notebooklm_bundles.py` creates local upload bundles in `exports/notebooklm/`.

Generated exports are ignored by Git because they duplicate source material already stored in `raw/`.

## Export

```bash
python3 scripts/export_notebooklm_bundles.py
```

Each topic becomes:

```text
exports/notebooklm/<topic-id>/
  00-guide.md
  manifest.json
  podcast_prompt.md
  sources/
```

For NotebookLM, upload `00-guide.md` and the files under `sources/`. Use `podcast_prompt.md` as the Audio Overview direction.

## Google Auth

Local export does not require Google login.

Creating real NotebookLM notebooks, uploading files, or generating Audio Overviews requires a Google session. Use an interactive browser login through NotebookLM or `notebooklm-py`; do not commit passwords, cookies, browser profiles, or generated auth state.
