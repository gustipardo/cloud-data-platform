-- Migration 099
-- Generated: 2026-10-18

CREATE INDEX IF NOT EXISTS idx_events_user_type_99
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
