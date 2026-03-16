-- Migration 056
-- Generated: 2026-03-16

CREATE INDEX IF NOT EXISTS idx_events_user_type_56
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
