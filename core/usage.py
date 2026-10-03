"""Per-turn token accounting. Create one Usage inside ask_stream and pass it
into each llm.complete. Do not keep this on the llm module: SSE runs each
request on its own thread, and a module list would mix those turns."""


class Usage:
    def __init__(self) -> None:
        self.calls: list[dict] = []

    def add(
        self,
        *,
        model: str,
        gear: str,
        prompt: int | None,
        completion: int | None,
        cache_hit: int | None,
        cache_miss: int | None,
        ms: float,
    ) -> None:
        self.calls.append({
            "model": model,
            "gear": gear,
            "prompt": prompt,
            "completion": completion,
            "cache_hit": cache_hit,
            "cache_miss": cache_miss,
            "ms": round(ms, 1),
        })

    def add_sdk(self, gear: str, model: str, usage, ms: float) -> None:
        if usage is None:
            self.add(model=model, gear=gear, prompt=None, completion=None,
                     cache_hit=None, cache_miss=None, ms=ms)
            return
        self.add(
            model=model,
            gear=gear,
            prompt=getattr(usage, "prompt_tokens", None),
            completion=getattr(usage, "completion_tokens", None),
            cache_hit=getattr(usage, "prompt_cache_hit_tokens", None),
            cache_miss=getattr(usage, "prompt_cache_miss_tokens", None),
            ms=ms,
        )

    def totals(self) -> dict:
        def _sum(key: str) -> int:
            return sum(c[key] or 0 for c in self.calls)

        return {
            "llm_calls": len(self.calls),
            "prompt_tokens": _sum("prompt"),
            "completion_tokens": _sum("completion"),
            "cache_hit_tokens": _sum("cache_hit"),
            "cache_miss_tokens": _sum("cache_miss"),
            "calls": list(self.calls),
        }
