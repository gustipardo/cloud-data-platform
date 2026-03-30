-- Migration 063
-- Generated: 2026-03-30

CREATE INDEX IF NOT EXISTS idx_events_user_type_63
    ON analytics.events (user_id, event_type)
    WHERE user_id IS NOT NULL;
