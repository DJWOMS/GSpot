import { useEffect, useState } from 'react'
import { useFormContext, Controller } from 'react-hook-form'
import { Group, Label } from 'components/Form'
import { SkeletonInput } from 'components/Skeleton'
import { Range } from 'components/Slider'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './Prices.module.scss'

type PriceState = number

const Prices = () => {
  const [defaultPrices, setDefaultPrices] = useState<PriceState[] | null>(null)
  const [prices, setPrices] = useState<PriceState[]>([])

  const { control } = useFormContext()

  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<PriceState[]>({
        path: '/games/filters/prices',
      })

      if (response) {
        setPrices(response)
        setDefaultPrices(response)
      }
    }

    loadData()
  }, [])

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
          <div className={s.range}>
            <div>{prices[0]}</div>
            <div>{prices[1]}</div>
          </div>

          <Controller
            control={control}
            name="prices"
            render={({ field: { onChange } }) => <Range min={0} max={1000} defaultValue={[100, 500]} onChange={onChange} />}
          />
        </>
      )}
    </Group>
  )
}

export { Prices }
