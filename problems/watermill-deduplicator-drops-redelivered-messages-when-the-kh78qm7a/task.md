There are issues with duplicate message processing in Watermill.

If processing fails or panics, resubmitting the same message should give it another chance to process.

When the same message comes in while the previous one is still being processed, the new one should wait.

If the first message finishes processing successfully, the second one should be cancelled.

If the first one fails, the waiting copy should be given another chance to process.

If the waiting copy is cancelled with its context, it should cancel waiting and return the cancellation error.

It should also stop waiting after the configured timeout and process the message, without letting the late result of the first copy affect anything that happened afterwards. The default timeout is one minute.

Publishing has similar problems if the same message is published at the same time. A successful Publish call should mean that all of its messages were published, either by this call, or the previous one.

A failed publish should still be able to publish the message.

Failed publishes and batches with a hashing error should not mark messages as published, and should finish overlapping batches properly.

DelayOnError should apply the multiplier accurately, including fractions, up to MaxInterval.

Throttle should return the context error when cancelled, and the delay metadata should never be shorter than requested, even for subsecond durations.