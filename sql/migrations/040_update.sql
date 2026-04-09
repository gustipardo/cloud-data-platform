-- Migration 040
-- Generated: 2026-04-09

CREATE INDEX IF NOT EXISTS idx_events_user_type_40
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
