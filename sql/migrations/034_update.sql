-- Migration 034
-- Generated: 2026-11-05

CREATE INDEX IF NOT EXISTS idx_events_user_type_34
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
