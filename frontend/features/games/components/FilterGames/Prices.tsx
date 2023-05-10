import { useEffect, useState } from 'react'
import { useFormContext, Controller } from 'react-hook-form'
import { Group, Label } from 'components/Form'
import { SkeletonInput } from 'components/Skeleton'
import { Range } from 'components/Slider'
import type { FilterPriceType } from 'features/games/types'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './Prices.module.css'

const Prices = () => {
  const [defaultPrices, setDefaultPrices] = useState<FilterPriceType | null>(null)
  const { control, setValue, getValues } = useFormContext()

  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<FilterPriceType>({
        path: '/games/filters/prices',
      })

      if (response) {
        setDefaultPrices(response)
      }
    }

    loadData()
  }, [getValues, setValue])

  return (
    <Group>
      <Label>Цена: </Label>

      {defaultPrices === null ? (
        <>
          <SkeletonInput size="28" />
          <SkeletonInput />
        </>
      ) : (
        <>
          <Controller
            control={control}
            name="prices"
            render={({ field: { onChange, value } }) => {
              const data = value?.length > 0 ? value : defaultPrices

              return (
                <>
                  <div className={s.range}>
                    <div>{data[0]}</div>
                    <div>{data[1]}</div>
                  </div>

                  <Range min={0} max={defaultPrices[1]} value={data} onChange={onChange} />
                </>
              )
            }}
          />
        </>
      )}
    </Group>
  )
}

export { Prices }
