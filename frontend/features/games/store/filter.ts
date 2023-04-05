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
  getFilter: (key: keyof FilterState) => any
  setFilter: (key: keyof FilterState, value: any) => void
  clearFilters: () => void
}

const initial = {
  keywords: '',
  sortby: '',
  prices: [],
  platforms: [],
  genres: [],
}

const useFilter = create<FilterStore>((set, get) => ({
  ...initial,
  setFilters: (queryParams) =>
    set({
      keywords: queryParams.get('keywords') ?? '',
      sortby: queryParams.get('sortby') ?? '',
      prices: queryParams.getAll('prices').map((price) => parseInt(price)) ?? [],
      platforms: queryParams.getAll('platforms') ?? [],
      genres: queryParams.getAll('genres') ?? [],
    }),
  setFilter: (key, value) =>
    set({
      [key]: value,
    }),
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
  getFilter: (key) => {
    return get()[key]
  },
  clearFilters: () => set(initial),
}))

export { useFilter }
