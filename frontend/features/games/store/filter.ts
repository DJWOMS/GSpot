import { create } from 'zustand'

interface FilterState {
  keywords: string
  sortby: string
  prices: number[]
  platforms: string[]
  genres: string[]
}

interface FilterStore extends FilterState {
  setFilters: (queryParams: URLSearchParams) => void
  getFilters: () => FilterState
  setFilter: (key: keyof FilterState, value: any) => void
  toggleFilter: (key: keyof FilterState, subkey: string, value: boolean) => void
}

const useFilter = create<FilterStore>((set, get) => ({
  keywords: '',
  sortby: '',
  prices: [],
  platforms: [],
  genres: [],
  setFilters: (queryParams) =>
    set({
      keywords: queryParams.get('keywords') ?? '',
      sortby: queryParams.get('sortby') ?? '',
      platforms: queryParams.getAll('platforms') ?? [],
      genres: queryParams.getAll('genres') ?? [],
    }),
  setFilter: (key, value) =>
    set(() => ({
      [key]: value,
    })),
  getFilters: () => {
    const { keywords, sortby, prices, platforms, genres } = get()
    return {
      keywords,
      sortby,
      platforms,
      prices,
      genres,
    }
  },
  toggleFilter: (key, subkey, value) =>
    set((state) => ({
      [key]: [...(Array.isArray(state[key]) ? state[key] : []), ...(value ? [subkey] : []).filter((k: string) => k !== '')],
    })),
}))

export { useFilter }
