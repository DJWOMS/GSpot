'use client'

import { useState } from 'react'
import { useForm } from 'react-hook-form'
import cn from 'classnames'
import { CheckBox } from 'components/Form'
// eslint-disable-next-line prettier/prettier
import Form from 'components/Form/Form'
// eslint-disable-next-line prettier/prettier
import Select from 'components/Select'
import { Range } from 'components/Slider'
import { useRouter, useSearchParams } from 'next/navigation'
import type {
  FilterGenreInterface,
  FilterPlatformInterface,
  FilterPriceType,
  FilterSortByInterface,
} from '../../types'
import s from './FilterGames.module.css'

interface FilterValues {
  sortby?: string
  prices?: number[]
  platforms: string[]
  genres: string[]
  subgenres: string[]
}

interface Props {
  sorts?: FilterSortByInterface[]
  platforms?: FilterPlatformInterface[]
  genres?: FilterGenreInterface[]
  prices?: FilterPriceType
}

const FilterGames = ({ sorts, platforms, genres, prices }: Props) => {
  const queryParams = useSearchParams()
  const { setValue } = useForm<FilterValues>({
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

  const onSubmitForm = (data: FilterValues) => {
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
        <Form
          fields={[
            {
              name: 'sortby',
              label: 'Сортировать:',
              rules: {},
              render: ({ field }) => (
                <Select
                  {...field}
                  options={sorts?.map((i) => ({ name: i.name, value: i.id }))}
                  value={field.value ? field.value.toString() : ''}
                />
              ),
            },
            {
              name: 'prices',
              label: 'Цена:',
              rules: {},
              render: ({ field: { onChange, value } }) => {
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
              },
            },
            {
              name: 'platforms',
              label: 'Платформа:',
              rules: {},
              render: ({ field }) => {
                if (!platforms) {
                  return <></>
                }
                return platforms.map(({ id, name }) => (
                  <CheckBox key={id} label={name} defaultValue={id} {...field} />
                ))
              },
            },
            {
              name: 'genres',
              label: 'Жанры:',
              rules: {},
              render: ({ field }) => {
                if (!genres) {
                  return <></>
                }
                // genres?: undefined | null[];
                const fieldValue = field.value || []
                return genres.map(({ id, name, subgenres }) => (
                  <>
                    <CheckBox
                      key={id}
                      onChange={() => onChangeCheckbox(fieldValue, field.onChange, id)}
                      label={name}
                      checked={checkboxValue(fieldValue, id)}
                    />
                    {fieldValue.includes(id.toString()) && subgenres.length && (
                      <div className="mb-5 ml-5">
                        {subgenres.map(({ id, name }) => (
                          <CheckBox
                            key={`s${id}`}
                            onChange={() => onChangeCheckbox(fieldValue, field.onChange, id, true)}
                            checked={checkboxValue(fieldValue, id)}
                            label={name}
                          />
                        ))}
                      </div>
                    )}
                  </>
                ))
              },
            },
          ]}
          title="Фильтры"
          onSubmit={onSubmitForm}
          btnText="Применить фильтр"
          config={{
            defaultValues: {
              sortby: undefined,
              prices: undefined,
              platforms: [],
              genres: [],
              subgenres: [],
            },
          }}
          onResetButton
          onResetSubmit
        />
      </div>
    </>
  )
}

export default FilterGames
