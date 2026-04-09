-- Supabase SQL Schema for IPL Predictor

-- 1. Create Users Table
CREATE TABLE public.users (
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    username text UNIQUE NOT NULL,
    name text,
    pin text NOT NULL,
    role text DEFAULT 'player'::text,
    is_nice_group boolean DEFAULT false,
    created_at timestamp with time zone DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 2. Create Matches Table
CREATE TABLE public.matches (
    id text PRIMARY KEY,
    name text NOT NULL,
    match_type text,
    status text,
    venue text,
    date date,
    start_time_iso timestamp with time zone,
    team1_name text,
    team1_short text,
    team2_name text,
    team2_short text,
    winner text, -- Null if not played yet, otherwise short name like 'MI'
    created_at timestamp with time zone DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 3. Create Picks Table
CREATE TABLE public.picks (
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id uuid REFERENCES public.users(id) ON DELETE CASCADE,
    match_id text REFERENCES public.matches(id) ON DELETE CASCADE,
    team_picked text NOT NULL,
    points numeric DEFAULT 0,
    created_at timestamp with time zone DEFAULT timezone('utc'::text, now()) NOT NULL,
    UNIQUE(user_id, match_id) -- A user can only pick once per match
);

-- Note: Configure Row Level Security (RLS) in the Supabase Dashboard
-- to securely limit row inserts/updates if desired. For the MVP,
-- you can enable anon public read/write while testing.
