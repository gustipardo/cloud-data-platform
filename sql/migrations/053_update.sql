-- Migration 053
-- Generated: 2026-03-20

CREATE INDEX IF NOT EXISTS idx_events_user_type_53
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
