-- Migration 018
-- Generated: 2026-05-20

CREATE INDEX IF NOT EXISTS idx_events_user_type_18
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
