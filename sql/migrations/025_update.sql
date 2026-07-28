-- Migration 025
-- Generated: 2026-07-28

CREATE INDEX IF NOT EXISTS idx_events_user_type_25
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
