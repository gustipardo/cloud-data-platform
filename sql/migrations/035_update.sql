-- Migration 035
-- Generated: 2026-07-12

CREATE INDEX IF NOT EXISTS idx_events_user_type_35
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
