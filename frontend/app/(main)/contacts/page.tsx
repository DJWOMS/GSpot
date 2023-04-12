'use client'

import { SubmitHandler, useForm } from 'react-hook-form'
import { Input } from 'components/Form'
import Section from 'components/Section'
import Link from 'next/link'
import s from './page.module.scss'

export interface IFormInputs {
  name: string
  email: string
  subject: string
  message: string
}

const ContactsPage = () => {
  const {
    register,
    formState: { errors },
    handleSubmit,
  } = useForm<IFormInputs>()
  const onSubmit: SubmitHandler<IFormInputs> = (data, e) => {
    e?.preventDefault()
    console.log(data)
    // alert(JSON.stringify(data))
    //reset()
  }
  //const finalClassName = s.formBtn + (disabled ? ' ' + s.disabled : '')
  //{...register('name', { required: false, minLength: 2 })}
  //{...register('email', {
  //                   required: 'Email is required',
  //                   pattern: {
  //                     value:
  //                       /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
  //                     message: 'Please enter a valid email',
  //                   },
  //                 })}
  return (
    <div>
      <Section title="Contacts" />
      <Section>
        <div className={s.row}>
          <div className={s.contactsForm}>
            <Section title="Contacts form" />
            <form onSubmit={handleSubmit(onSubmit)} action="#" className={s.form}>
              <div>
                <div>
                  {' '}
                  <Input type="text" id="name" placeholder="Name" aria-invalid={errors.name ? 'true' : 'false'} />
                </div>
                <div>
                  {' '}
                  <Input type="email" placeholder="Email" />
                  {errors?.email && <span>{errors.email.message}</span>}
                </div>
                <div>
                  <Input type="text" placeholder="Subject" />
                </div>
                <div>
                  <textarea className={s.formTextarea} placeholder="Type your message..."></textarea>
                </div>
                <button className={s.formBtn} type="submit">
                  Send
                </button>
              </div>
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
      </Section>
    </div>
  )
}

export default ContactsPage
