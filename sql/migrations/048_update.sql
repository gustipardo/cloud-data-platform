-- Migration 048
-- Generated: 2026-09-19

CREATE INDEX IF NOT EXISTS idx_events_user_type_48
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
