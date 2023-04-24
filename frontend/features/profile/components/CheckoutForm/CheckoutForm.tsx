'use client'

import { Controller, useForm } from 'react-hook-form'
import { ErrorMessage } from '@hookform/error-message'
import { Input, Select } from 'components/Form'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './CheckoutForm.module.scss'

const CheckoutForm = () => {
  const {
    handleSubmit,
    control,
    formState: { errors },
  } = useForm()

  const onSubmitCheckout = async (data: any) => {
    const response = await fetchServerSide({
      path: '/profile/checkout',
      method: 'POST',
      body: JSON.stringify(data),
    })
    if (response) {
      console.log(response)
    }
  }

  return (
    <div>
      <form action="#" className={s.form} onSubmit={handleSubmit(onSubmitCheckout)}>
        <Controller
          control={control}
          name="fullName"
          defaultValue=""
          rules={{ required: true }}
          render={({ field }) => {
            return <Input {...field} type="text" className={s.formInput} placeholder="John Doe" />
          }}
        />
        <ErrorMessage errors={errors} name="fullName" render={({ message }) => <p>{message}</p>} />
        <Controller
          control={control}
          name="email"
          defaultValue=""
          rules={{ required: true }}
          render={({ field }) => {
            return <Input {...field} type="email" className={s.formInput} placeholder="gg@template.by" />
          }}
        />
        <ErrorMessage errors={errors} name="email" render={({ message }) => <p>{message}</p>} />
        <Controller
          control={control}
          name="phoneNumber"
          defaultValue=""
          rules={{ required: true }}
          render={({ field }) => {
            return <Input {...field} type="text" className={s.formInput} placeholder="+1 234 567-89-00" />
          }}
        />
        <ErrorMessage errors={errors} name="phoneNumber" render={({ message }) => <p>{message}</p>} />
        <Controller
          control={control}
          name="paymentMethod"
          defaultValue="visa"
          rules={{ required: true }}
          render={({ field }) => {
            return (
              <Select className={s.formSelect} {...field}>
                <option value="visa">Visa</option>
                <option value="mastercard">Mastercard</option>
                <option value="qiwi">Qiwi</option>
              </Select>
            )
          }}
        />
        <ErrorMessage errors={errors} name="paymentMethod" render={({ message }) => <p>{message}</p>} />
        <span className={s.formText}>
          There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.
        </span>
        <input type="submit" className={s.formBtn} />
      </form>
    </div>
  )
}

export { CheckoutForm }
