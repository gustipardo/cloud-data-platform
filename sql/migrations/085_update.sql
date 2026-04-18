-- Migration 085
-- Generated: 2026-04-18

CREATE INDEX IF NOT EXISTS idx_events_user_type_85
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
