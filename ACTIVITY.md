# Activity

Append activity log at bottom. Follow the template:

```markdown
### Current atetime in YYYY-MM-DD HH:MM format for Central European Timezone (use tools)

**Tasks completed:** Tasks that are already completed; take ID and description from @SPEC.md.

**Current tasks:** Task that is implemented in the current instance; take description from @SPEC.md.

**Blockers:** Issues encountered.
```

## Session Log

### 2026-02-01 15:20 (CET)

**Tasks completed:** None (first task)

**Current task:** US-1 - Add logging configuration settings to config.py

**Changes made:**
- Modified `src/semantic_scholar_mcp/config.py`
- Added `log_level` setting with `SS_LOG_LEVEL` env var (default: INFO)
- Added `log_format` setting with `SS_LOG_FORMAT` env var (default: simple)
- Updated class docstring with new attributes

**Verification:**
- ruff format: PASS
- ruff check: PASS (6 auto-fixed issues from pre-existing code)
- ty check: PASS (2 pre-existing type errors unrelated to changes)
- pytest: PASS (132 passed)

**Blockers:** None

### 2026-02-01 15:27 (CET)

**Tasks completed:** US-1 - Add logging configuration settings to config.py

**Current task:** US-2 - Create logging_config.py module

**Changes made:**
- Created `src/semantic_scholar_mcp/logging_config.py`
- Implemented `setup_logging()` function with level and format_style parameters
- Implemented `get_logger(name)` function returning namespaced logger
- Supports "simple" and "detailed" format styles
- Uses settings from config.py for defaults

**Verification:**
- ruff format: PASS (1 file reformatted)
- ruff check: PASS
- ty check: PASS (2 pre-existing type errors unrelated to changes)
- pytest: PASS (132 passed)

**Blockers:** None

### 2026-02-01 16:14 (CET)

**Tasks completed:** US-1, US-2

**Current task:** US-3 - Add logging to paper_tracker.py

**Changes made:**
- Modified `src/semantic_scholar_mcp/paper_tracker.py`
- Imported `get_logger` from `logging_config`
- Added DEBUG log in `track()` method for paper tracking
- Added DEBUG log in `track_many()` method with count of papers
- Added INFO log in `clear()` method with count of cleared papers

**Verification:**
- ruff format: PASS
- ruff check: PASS
- ty check: PASS (2 pre-existing type errors unrelated to changes)
- pytest: PASS (132 passed)

**Blockers:** None

### 2026-02-01 16:16 (CET)

**Tasks completed:** US-1, US-2, US-3

**Current task:** US-4 - Add logging to bibtex.py

**Changes made:**
- Modified `src/semantic_scholar_mcp/bibtex.py`
- Imported `get_logger` from `logging_config`
- Added DEBUG log in `paper_to_bibtex_entry()` for entry generation
- Added INFO log in `export_papers_to_bibtex()` with count of exported entries

**Verification:**
- ruff format: PASS
- ruff check: PASS
- ty check: PASS (2 pre-existing type errors unrelated to changes)
- pytest: PASS (132 passed)

**Blockers:** None

### 2026-02-01 16:17 (CET)

**Tasks completed:** US-1, US-2, US-3, US-4

**Current task:** US-5 - Add new exception classes to exceptions.py

**Changes made:**
- Modified `src/semantic_scholar_mcp/exceptions.py`
- Added `ServerError` class with `status_code` attribute for 5xx errors
- Added `AuthenticationError` class for 401/403 errors
- Added `ConnectionError` class for network/timeout issues

**Verification:**
- ruff format: PASS
- ruff check: PASS
- ty check: PASS (2 pre-existing type errors unrelated to changes)
- pytest: PASS (132 passed)

**Blockers:** None

### 2026-02-01 16:20 (CET)

**Tasks completed:** US-1, US-2, US-3, US-4, US-5

**Current task:** US-6 - Improve _handle_response() error handling in client.py

**Changes made:**
- Modified `src/semantic_scholar_mcp/client.py`
  - Updated imports to include `AuthenticationError` and `ServerError`
  - Refactored `_handle_response()` to check success first (status < 400)
  - Added `AuthenticationError` for 401/403 errors with helpful message
  - Added `ServerError` for 5xx errors with `status_code` attribute
  - Updated error messages to include endpoint context
  - Improved `RateLimitError` and `NotFoundError` messages with format hints
- Modified `tests/test_client.py`
  - Added imports for `AuthenticationError` and `ServerError`
  - Updated `test_http_429_raises_rate_limit_error_with_informative_message` to match new message format
  - Renamed `test_http_500_raises_semantic_scholar_error` to `test_http_500_raises_server_error`
  - Added `TestAuthenticationError` class with tests for 401 and 403 responses

**Verification:**
- ruff format: PASS
- ruff check: PASS
- ty check: PASS (2 pre-existing type errors unrelated to changes)
- pytest: PASS (134 passed - 2 new tests added)

**Blockers:** None
