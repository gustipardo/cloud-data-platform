-- Migration 076
-- Generated: 2026-07-14

CREATE INDEX IF NOT EXISTS idx_events_user_type_76
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
