import { Input } from 'components/Form'
import Section from 'components/Section'
import Link from 'next/link'
import s from './page.module.scss'

const ContactsPage = () => {
  return (
    <div>
      <Section title="Contacts" />
      <div className={s.row}>
        <div className={s.contactsForm}>
          <Section title="Contacts form" />
          <form action="#" className={s.form}>
            <Input type="text" placeholder="Name" />
            <Input type="email" placeholder="Email" />
            <Input type="text" placeholder="Subject" />
            <textarea className={s.formTextarea} placeholder="Type your message..."></textarea>
            <button type="button" className={s.formBtn}>
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
