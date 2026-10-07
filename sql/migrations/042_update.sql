-- Migration 042
-- Generated: 2026-10-07

CREATE INDEX IF NOT EXISTS idx_events_user_type_42
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
