-- Migration 012
-- Generated: 2026-05-27

CREATE INDEX IF NOT EXISTS idx_events_user_type_12
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
