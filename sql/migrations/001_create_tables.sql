-- ============================================
-- Migration 001: Create base tables
-- Database: PostgreSQL (RDS)
-- Created: 2025-02-15
-- ============================================

CREATE SCHEMA IF NOT EXISTS analytics;

-- Events fact table
CREATE TABLE analytics.events (
    id              BIGSERIAL PRIMARY KEY,
    event_id        VARCHAR(64) NOT NULL UNIQUE,
    event_type      VARCHAR(100) NOT NULL,
    category        VARCHAR(50) NOT NULL,
    action          VARCHAR(50) NOT NULL,
    user_id         VARCHAR(128),
    payload         JSONB NOT NULL DEFAULT '{}',
    metadata        JSONB DEFAULT '{}',
    source_key      VARCHAR(512),
    processed_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    event_timestamp TIMESTAMPTZ NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes for common query patterns
CREATE INDEX idx_events_type ON analytics.events (event_type);
CREATE INDEX idx_events_user ON analytics.events (user_id) WHERE user_id IS NOT NULL;
CREATE INDEX idx_events_timestamp ON analytics.events (event_timestamp DESC);
CREATE INDEX idx_events_category ON analytics.events (category, action);
CREATE INDEX idx_events_payload ON analytics.events USING GIN (payload);

-- Daily aggregation table
CREATE TABLE analytics.daily_stats (
    id          SERIAL PRIMARY KEY,
    stat_date   DATE NOT NULL,
    event_type  VARCHAR(100) NOT NULL,
    event_count BIGINT NOT NULL DEFAULT 0,
    unique_users BIGINT NOT NULL DEFAULT 0,
    avg_payload_size NUMERIC(10, 2),
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE (stat_date, event_type)
);

CREATE INDEX idx_daily_stats_date ON analytics.daily_stats (stat_date DESC);

-- User sessions table
CREATE TABLE analytics.user_sessions (
    id              BIGSERIAL PRIMARY KEY,
    session_id      VARCHAR(128) NOT NULL UNIQUE,
    user_id         VARCHAR(128) NOT NULL,
    started_at      TIMESTAMPTZ NOT NULL,
    ended_at        TIMESTAMPTZ,
    duration_seconds INTEGER,
    event_count     INTEGER NOT NULL DEFAULT 0,
    metadata        JSONB DEFAULT '{}',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_sessions_user ON analytics.user_sessions (user_id);
CREATE INDEX idx_sessions_started ON analytics.user_sessions (started_at DESC);

-- Error tracking table
CREATE TABLE analytics.error_log (
    id              BIGSERIAL PRIMARY KEY,
    error_type      VARCHAR(200) NOT NULL,
    error_message   TEXT,
    stack_trace     TEXT,
    source_function VARCHAR(200),
    event_id        VARCHAR(64),
    context         JSONB DEFAULT '{}',
    severity        VARCHAR(20) NOT NULL DEFAULT 'ERROR',
    resolved        BOOLEAN NOT NULL DEFAULT FALSE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_errors_type ON analytics.error_log (error_type);
CREATE INDEX idx_errors_severity ON analytics.error_log (severity) WHERE NOT resolved;
CREATE INDEX idx_errors_created ON analytics.error_log (created_at DESC);
