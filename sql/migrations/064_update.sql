-- Migration 064
-- Generated: 2026-05-21

CREATE INDEX IF NOT EXISTS idx_events_user_type_64
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
