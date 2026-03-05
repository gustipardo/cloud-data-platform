-- Migration 031
-- Generated: 2026-03-05

CREATE INDEX IF NOT EXISTS idx_events_user_type_31
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
