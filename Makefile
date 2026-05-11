all: sync run

run:
	uv run run.py

sync:
	uv sync

lock:
	uv lock
