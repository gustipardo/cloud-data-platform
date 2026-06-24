-- Migration 044
-- Generated: 2026-06-24

CREATE INDEX IF NOT EXISTS idx_events_user_type_44
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
