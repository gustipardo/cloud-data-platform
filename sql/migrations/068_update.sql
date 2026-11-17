-- Migration 068
-- Generated: 2026-11-17

CREATE INDEX IF NOT EXISTS idx_events_user_type_68
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
