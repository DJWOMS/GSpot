'use client'

import { useState } from 'react'
import { useForm, FormProvider, SubmitHandler } from 'react-hook-form'
import cn from 'classnames'
import { Group } from 'components/Form'
import { useRouter, useSearchParams } from 'next/navigation'
import qs from 'qs'
import s from './FilterGames.module.css'
import { Genres } from './Genres'
import { Platforms } from './Platforms'
import { Prices } from './Prices'
import { SortBy } from './SortBy'

interface FilterValues {
  sortby: string | null
  prices: number[] | null
  platforms: string[]
  genres: string[]
  subgenres: string[]
}

const initalFilterState: FilterValues = {
  sortby: null,
  prices: null,
  platforms: [],
  genres: [],
  subgenres: [],
}

const FilterGames = () => {
  const queryParams = useSearchParams()
  const form = useForm<FilterValues>({
    defaultValues: {
      sortby: queryParams.get('sortby'),
      prices: queryParams.getAll('prices').map((p) => parseInt(p)),
      platforms: queryParams.getAll('platforms'),
      genres: queryParams.getAll('genres'),
      subgenres: queryParams.getAll('subgenres'),
    },
  })

  // update router if needed
  const router = useRouter()

  const onSubmitForm: SubmitHandler<FilterValues> = (data) =>
    router.push(
      `/catalog?${qs.stringify(data, {
        arrayFormat: 'repeat',
        skipNulls: true,
      })}`
    )

  const [openMobileFilter, setOpenMobileFilter] = useState(false)
  const toggleMobileFilter = () => setOpenMobileFilter((state) => !state)

  return (
    <>
      <button className={s.openFilter} onClick={toggleMobileFilter}>
        {!openMobileFilter ? 'Открыть фильтр' : 'Скрыть фильтр'}
      </button>

      <div className={cn(s.wrapper, { [s.open]: openMobileFilter })}>
        <FormProvider {...form}>
          <form onSubmit={form.handleSubmit(onSubmitForm)} className={s.components}>
            <h4 className={s.title}>
              Фильтры
              <button className={s.clearFilters} onClick={() => form.reset(initalFilterState)} type="button">
                Сбросить
              </button>
            </h4>

            <SortBy />
            <Prices />
            <Platforms />
            <Genres />

            <Group>
              <button className={s.applyFilter} type="submit">
                Применить фильтр
              </button>
            </Group>
          </form>
        </FormProvider>
      </div>
    </>
  )
}

export { FilterGames }
