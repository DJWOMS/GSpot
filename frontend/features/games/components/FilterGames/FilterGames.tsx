'use client'

import { FC, useState } from 'react'
import { useForm, SubmitHandler, Controller } from 'react-hook-form'
import cn from 'classnames'
import { CheckBox, Group } from 'components/Form'
import Select from 'components/Select'
import { Range } from 'components/Slider'
import type {
  FilterGenreInterface,
  FilterPlatformInterface,
  FilterPriceType,
  FilterSortByInterface,
} from 'features/games/types'
import { useRouter, useSearchParams } from 'next/navigation'
import s from './FilterGames.module.css'
import GroupItem from './GroupItem'

interface FilterValues {
  sortby?: string
  prices?: number[]
  platforms: string[]
  genres: string[]
  subgenres: string[]
}

const initalFilterState: FilterValues = {
  sortby: undefined,
  prices: undefined,
  platforms: [],
  genres: [],
  subgenres: [],
}

interface Props {
  sorts?: FilterSortByInterface[]
  platforms?: FilterPlatformInterface[]
  genres?: FilterGenreInterface[]
  prices?: FilterPriceType
}

const FilterGames: FC<Props> = ({ sorts, platforms, genres, prices }) => {
  const queryParams = useSearchParams()
  const { control, handleSubmit, reset, setValue } = useForm<FilterValues>({
    defaultValues: {
      sortby: queryParams.get('sortby') ?? undefined,
      prices: queryParams.getAll('prices').map((p) => parseInt(p)),
      platforms: queryParams.getAll('platforms'),
      genres: queryParams.getAll('genres'),
      subgenres: queryParams.getAll('subgenres'),
    },
  })

  // update router if needed
  const router = useRouter()

  const onSubmitForm: SubmitHandler<FilterValues> = (data) => {
    const params = new URLSearchParams()
    Object.entries(data).forEach(([k, v]) => {
      if (v) {
        params.append(k, v)
      }
    })
    router.push(`/catalog?${params.toString()}`)
  }

  const onChangeCheckbox = (
    values: string[],
    onChange: (value: string[]) => void,
    id: number,
    isSubgenres = false
  ) => {
    if (values.includes(id.toString())) {
      if (!isSubgenres) {
        setValue('subgenres', [])
      }
      return onChange(
        values.filter((i) => {
          return i !== id.toString()
        })
      )
    }
    onChange([...values, id.toString()])
  }

  const checkboxValue = (values: string[], id: number) => !!values.find((i) => i === id.toString())

  const [openMobileFilter, setOpenMobileFilter] = useState(false)
  const toggleMobileFilter = () => setOpenMobileFilter((state) => !state)

  return (
    <>
      <button className={s.openFilter} onClick={toggleMobileFilter}>
        {!openMobileFilter ? 'Открыть фильтр' : 'Скрыть фильтр'}
      </button>

      <div className={cn(s.wrapper, { [s.open]: openMobileFilter })}>
        <form onSubmit={handleSubmit(onSubmitForm)} className={s.components}>
          <div className={s.header}>
            <h4>Фильтры</h4>
            <button className={s.clearFilters} onClick={() => reset(initalFilterState)} type="button">
              Сбросить
            </button>
          </div>

          <GroupItem label="Сортировать:">
            <Controller
              name="sortby"
              control={control}
              render={({ field }) => (
                <Select {...field} options={sorts?.map((i) => ({ name: i.name, value: i.id }))} />
              )}
            />
          </GroupItem>

          <GroupItem label="Цена:">
            <Controller
              control={control}
              name="prices"
              render={({ field: { onChange, value } }) => {
                const data = value?.length ? value : prices

                return (
                  <>
                    <div className={s.rangeBox}>
                      {data && (
                        <>
                          <input
                            type="number"
                            className={s.range}
                            value={data[0]}
                            onChange={(e) => onChange([e.target.value, data[1]])}
                          />
                          <span className={s.separator}>-</span>
                          <input
                            type="number"
                            className={s.range}
                            value={data[1]}
                            max={prices ? prices[1] : 0}
                            onChange={(e) => onChange([data[0], e.target.value])}
                          />
                        </>
                      )}
                    </div>

                    <Range
                      className={s.slider}
                      min={0}
                      max={prices ? prices[1] : 0}
                      value={data}
                      onChange={onChange}
                    />
                  </>
                )
              }}
            />
          </GroupItem>

          <GroupItem label="Платформа:">
            {platforms?.map(({ id, name }) => (
              <Controller
                key={id}
                control={control}
                name="platforms"
                render={({ field }) => <CheckBox label={name} defaultValue={id} {...field} />}
              />
            ))}
          </GroupItem>

          <GroupItem label="Жанры:">
            {genres?.map(({ id, name, subgenres }) => (
              <>
                <Controller
                  control={control}
                  name="genres"
                  render={({ field }) => (
                    <>
                      <CheckBox
                        onChange={() => onChangeCheckbox(field.value, field.onChange, id)}
                        label={name}
                        checked={checkboxValue(field.value, id)}
                      />
                      {field.value.includes(id.toString()) && subgenres.length && (
                        <div className="mb-5 ml-5">
                          {subgenres.map(({ id, name }) => (
                            <Controller
                              key={`s${id}`}
                              control={control}
                              name="subgenres"
                              render={({ field }) => (
                                <CheckBox
                                  onChange={() => onChangeCheckbox(field.value, field.onChange, id, true)}
                                  checked={checkboxValue(field.value, id)}
                                  label={name}
                                />
                              )}
                            />
                          ))}
                        </div>
                      )}
                    </>
                  )}
                />
              </>
            ))}
          </GroupItem>

          <Group>
            <button className={s.applyFilter} type="submit">
              Применить фильтр
            </button>
          </Group>
        </form>
      </div>
    </>
  )
}

export default FilterGames
