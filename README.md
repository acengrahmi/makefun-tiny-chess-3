# Tiny Chess v3 — 4 KB Python Chess Engine

Deterministic node-budget chess engine (4,095 bytes): 0x88 mailbox, negamax with PVS + LMR, alpha-beta, transposition table with exact/lower/upper bounds, quiescence search, MVV-LVA ordering, material + piece-square evaluation. No wall clock — move choice depends only on node budget and ply, so trials replay deterministically.

Local results: perft exact (startpos d4 197,281; kiwipete d3 97,862), 8.0/8 vs fixed-depth-3 baseline, kit trial-0 Elo 1,191.

make.fun competition: tiny-chess-01. Entry by @acengrahmi.
