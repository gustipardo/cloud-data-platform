-- Migration 082
-- Generated: 2026-10-26

CREATE INDEX IF NOT EXISTS idx_events_user_type_82
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
