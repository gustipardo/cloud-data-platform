-- Migration 011
-- Generated: 2026-05-08

CREATE INDEX IF NOT EXISTS idx_events_user_type_11
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
