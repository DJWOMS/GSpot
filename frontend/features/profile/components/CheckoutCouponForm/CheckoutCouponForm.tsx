'use client'

import { useState } from 'react'
import { Controller, useForm } from 'react-hook-form'
import { ErrorMessage } from '@hookform/error-message'
import { Input } from 'components/Form'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './CheckoutCouponForm.module.scss'

const CheckoutCouponForm = () => {
  const {
    handleSubmit,
    control,
    formState: { errors },
  } = useForm()
  const [coupon, setCoupon] = useState(false)
  const [couponInvalid, setCouponInvalid] = useState(false)

  const onSubmitCoupon = async (data: any) => {
    const response = await fetchServerSide({
      path: '/profile/checkout/coupon',
      method: 'POST',
      body: JSON.stringify(data),
    })
    if (response === true) {
      setCoupon(true)
      console.log(data)
    } else if (response === false) {
      setCouponInvalid(true)
      console.log(data)
    } else {
      console.log(data)
    }
  }

  return (
    <>
      <form action="#" className={s.form} onSubmit={handleSubmit(onSubmitCoupon)} target="dummyface">
        <Controller
          control={control}
          name="coupon"
          defaultValue=""
          render={({ field }) => {
            return <Input {...field} placeholder="Coupon code" />
          }}
        />
        <ErrorMessage errors={errors} name="couponError" render={({ message }) => <p>{message}</p>} />
        <input type="submit" className={s.formBtn} value="Применить" />
        {coupon && <p className={s.coupon}>Купон активирован</p>}
        {couponInvalid && <p className={s.couponInvalid}>Некорректный купон</p>}
      </form>
    </>
  )
}

export { CheckoutCouponForm }
