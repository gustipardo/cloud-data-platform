-- Migration 078
-- Generated: 2026-07-23

CREATE INDEX IF NOT EXISTS idx_events_user_type_78
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
