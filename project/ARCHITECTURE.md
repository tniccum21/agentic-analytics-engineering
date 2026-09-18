# Architecture Target

The project deliberately separates four responsibilities.

## Control plane

Owns durable state, lifecycle, stage boundaries, budgets, checkpointing, retries, approval/promotion gates, and terminal states.

## Agent harness

May own bounded model↔tool interaction inside selected stages. It does not get unbounded authority over lifecycle or production configuration changes.

## Hands / capability layer

Schema discovery, SQL execution, metadata retrieval, and later MCP calls. These are replaceable behind interfaces.

## Evaluation and improvement plane

Evaluates completed runs, clusters failures, proposes configuration changes, evaluates challengers, and promotes only through explicit gates.
