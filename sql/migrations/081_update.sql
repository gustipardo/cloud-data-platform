-- Migration 081
-- Generated: 2026-08-18

CREATE INDEX IF NOT EXISTS idx_events_user_type_81
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
