-- Migration 030
-- Generated: 2026-03-09

CREATE INDEX IF NOT EXISTS idx_events_user_type_30
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
