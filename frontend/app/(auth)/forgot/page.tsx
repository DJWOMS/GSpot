'use client'

import { Form, SignGroup, SignInput, SignBtn, SignText } from '../Form'

export default function Forgot() {
    return (
        <Form onSubmit={() => console.log('hello')}>
            <SignGroup>
                <SignInput type="text" placeholder="Введите ваш email" />
            </SignGroup>

            <SignBtn>Продолжить</SignBtn>

            <SignText>На указанный email будет отправлен код для сброса пароля.</SignText>
        </Form>
    )
}
