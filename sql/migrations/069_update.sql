-- Migration 069
-- Generated: 2026-06-26

CREATE INDEX IF NOT EXISTS idx_events_user_type_69
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
