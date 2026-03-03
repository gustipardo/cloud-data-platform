-- Migration 065
-- Generated: 2026-03-03

CREATE INDEX IF NOT EXISTS idx_events_user_type_65
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
