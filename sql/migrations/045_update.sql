-- Migration 045
-- Generated: 2026-08-16

CREATE INDEX IF NOT EXISTS idx_events_user_type_45
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
