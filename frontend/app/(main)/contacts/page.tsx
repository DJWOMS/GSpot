'use client'

import { SubmitHandler, useForm } from 'react-hook-form'
import { Input } from 'components/Form'
import Section from 'components/Section'
import Link from 'next/link'
import s from './page.module.scss'

interface IFormInputs {
  name: string
  email: string
  subject: string
  message: string
}
const ContactsPage = (disabled: any) => {
  const {
    register,
    formState: { errors },
    reset,
    handleSubmit,
  } = useForm<IFormInputs>()
  const onSubmit: SubmitHandler<IFormInputs> = (data) => {
    alert(JSON.stringify(data))
    reset()
  }
  const finalClassName = s.formBtn + (disabled ? ' ' + s.disabled : '')

  return (
    <div>
      <Section title="Contacts" />
      <div className={s.row}>
        <div className={s.contactsForm}>
          <Section title="Contacts form" />
          <form onSubmit={handleSubmit(onSubmit)} action="#" className={s.form}>
            <Input type="text" placeholder="Name" {...register('name', { required: true, minLength: 2 })} />
            <Input
              type="email"
              placeholder="Email"
              {...register('email', {
                required: 'Email is required',
                pattern: {
                  value:
                    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
                  message: 'Please enter a valid email',
                },
              })}
            />{' '}
            {errors.email && <span role="alert">{errors.email.message}</span>}
            <Input type="text" placeholder="Subject" {...register('subject', { required: true, minLength: 2 })} />
            <textarea
              className={s.formTextarea}
              placeholder="Type your message..."
              {...register('message', { required: true, minLength: 2 })}
            ></textarea>
            <button className={finalClassName} type="submit">
              Send
            </button>
          </form>
        </div>
        <div>
          <Section title="Info" />
          <div className={s.contactsInfo}>
            <p className={s.contacts}>
              {' '}
              It is a long fact that a reader will be distracted by the readable content of a page when looking at its layout.
            </p>
            <ul>
              <li className={s.contactsList}>
                <Link href="tel:+18092345678">+1 809 234-56-78</Link>
              </li>
              <li className={s.contactsList}>
                <Link href="mailto:support@gg.template">support@gg.template</Link>
              </li>
              <li className={s.contactsList}>
                <Link
                  href="https://maps.google.com/maps?q=221B+Baker+Street,+London,+United+Kingdom&amp;hl=en&amp;t=v&amp;hnear=221B+Baker+St,+London+NW1+6XE,+United+Kingdom"
                  className="open-map"
                >
                  221B Baker St, Marylebone, London
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ContactsPage
