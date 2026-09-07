-- Migration 076
-- Generated: 2026-09-07

CREATE INDEX IF NOT EXISTS idx_events_user_type_76
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
