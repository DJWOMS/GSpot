'use client'

import { useState } from 'react'
import { useForm, FormProvider, SubmitHandler } from 'react-hook-form'
import cn from 'classnames'
import { Group } from 'components/Form'
import { useRouter, useSearchParams } from 'next/navigation'
import qs from 'qs'
import s from './FilterGames.module.scss'
import { Genres } from './Genres'
import { Platforms } from './Platforms'
import { Prices } from './Prices'
import { SortBy } from './SortBy'

interface FilterValues {
  sortby: string | null
  prices: string[] | null
  platforms: string[]
  genres: string[]
}

const FilterGames = () => {
  const queryParams = useSearchParams()
  const form = useForm<FilterValues>({
    defaultValues: {
      sortby: queryParams.get('sortby'),
      prices: queryParams.getAll('prices'),
      genres: queryParams.getAll('genres'),
      platforms: queryParams.getAll('platforms'),
    },
  })

  // update router if needed
  const router = useRouter()

  const onSubmitForm: SubmitHandler<FilterValues> = ({ sortby, prices, platforms, genres }) =>
    router.push(`/catalog?${qs.stringify({ sortby, prices, platforms, genres }, { arrayFormat: 'repeat', skipNulls: true })}`)

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
            <h4 className={s.title}>Фильтры</h4>

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
