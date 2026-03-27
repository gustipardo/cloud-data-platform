-- ============================================
-- Analytics Queries
-- Common queries for reporting and analysis
-- ============================================

-- Events per day by type (last 30 days)
SELECT
    DATE(event_timestamp) AS event_date,
    event_type,
    COUNT(*) AS event_count,
    COUNT(DISTINCT user_id) AS unique_users
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '30 days'
GROUP BY DATE(event_timestamp), event_type
ORDER BY event_date DESC, event_count DESC;

-- Top event types
SELECT
    event_type,
    COUNT(*) AS total_count,
    COUNT(DISTINCT user_id) AS unique_users,
    MIN(event_timestamp) AS first_seen,
    MAX(event_timestamp) AS last_seen
FROM analytics.events
GROUP BY event_type
ORDER BY total_count DESC;

-- Hourly event distribution
SELECT
    EXTRACT(HOUR FROM event_timestamp) AS hour_of_day,
    COUNT(*) AS event_count,
    ROUND(AVG(COUNT(*)) OVER (), 2) AS avg_hourly
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY EXTRACT(HOUR FROM event_timestamp)
ORDER BY hour_of_day;

-- User activity summary
SELECT
    user_id,
    COUNT(*) AS total_events,
    COUNT(DISTINCT event_type) AS event_types_used,
    MIN(event_timestamp) AS first_activity,
    MAX(event_timestamp) AS last_activity,
    MAX(event_timestamp) - MIN(event_timestamp) AS active_period
FROM analytics.events
WHERE user_id IS NOT NULL
GROUP BY user_id
ORDER BY total_events DESC
LIMIT 100;

-- Error rate by function
SELECT
    source_function,
    severity,
    COUNT(*) AS error_count,
    COUNT(*) FILTER (WHERE NOT resolved) AS unresolved,
    MAX(created_at) AS last_occurrence
FROM analytics.error_log
WHERE created_at >= NOW() - INTERVAL '7 days'
GROUP BY source_function, severity
ORDER BY error_count DESC;

-- Session duration statistics
SELECT
    DATE(started_at) AS session_date,
    COUNT(*) AS total_sessions,
    ROUND(AVG(duration_seconds)) AS avg_duration_sec,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_seconds)) AS median_duration,
    ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY duration_seconds)) AS p95_duration,
    SUM(event_count) AS total_events
FROM analytics.user_sessions
WHERE started_at >= NOW() - INTERVAL '30 days'
    AND duration_seconds IS NOT NULL
GROUP BY DATE(started_at)
ORDER BY session_date DESC;

-- Funnel analysis: signup → first order
WITH user_signups AS (
    SELECT user_id, MIN(event_timestamp) AS signup_time
    FROM analytics.events
    WHERE event_type = 'user.signup'
    GROUP BY user_id
),
first_orders AS (
    SELECT user_id, MIN(event_timestamp) AS first_order_time
    FROM analytics.events
    WHERE event_type = 'order.created'
    GROUP BY user_id
)
SELECT
    COUNT(s.user_id) AS total_signups,
    COUNT(o.user_id) AS converted_users,
    ROUND(100.0 * COUNT(o.user_id) / NULLIF(COUNT(s.user_id), 0), 2) AS conversion_rate,
    ROUND(AVG(EXTRACT(EPOCH FROM (o.first_order_time - s.signup_time)) / 3600), 1) AS avg_hours_to_convert
FROM user_signups s
LEFT JOIN first_orders o ON s.user_id = o.user_id;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;

-- Query: Events processed per hour
SELECT
    DATE_TRUNC('hour', event_timestamp) AS hour,
    COUNT(*) AS events
FROM analytics.events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1 DESC;
