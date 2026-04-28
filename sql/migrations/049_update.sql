-- Migration 049
-- Generated: 2026-04-28

CREATE INDEX IF NOT EXISTS idx_events_user_type_49
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
